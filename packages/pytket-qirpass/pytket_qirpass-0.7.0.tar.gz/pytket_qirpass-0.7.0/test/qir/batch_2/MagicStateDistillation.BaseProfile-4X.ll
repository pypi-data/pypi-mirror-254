
%Range = type { i64, i64, i64 }
%Qubit = type opaque
%Result = type opaque
%Array = type opaque
%Tuple = type opaque
%String = type opaque

@PauliI = internal constant i2 0
@PauliX = internal constant i2 1
@PauliY = internal constant i2 -1
@PauliZ = internal constant i2 -2
@EmptyRange = internal constant %Range { i64 0, i64 1, i64 -1 }
@0 = internal constant [3 x i8] c"()\00"

define internal void @Microsoft__Quantum__Samples__Distill__body(i64 %maxNIterations, %Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4) {
entry:
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q0)
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q1)
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q2)
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q3)
  call void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %q4)
  call void @Microsoft__Quantum__Samples__Encode__adj(%Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4)
  %s0 = call %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %q1)
  %s1 = call %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %q2)
  %s2 = call %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %q3)
  %s3 = call %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %q4)
  %0 = icmp sgt i64 %maxNIterations, 1
  br i1 %0, label %condTrue__1, label %condContinue__1

condTrue__1:                                      ; preds = %entry
  %1 = call %Result* @__quantum__rt__result_get_zero()
  %2 = call i1 @__quantum__rt__result_equal(%Result* %s0, %Result* %1)
  %3 = xor i1 %2, true
  %4 = xor i1 %3, true
  br i1 %4, label %condTrue__2, label %condContinue__2

condTrue__2:                                      ; preds = %condTrue__1
  %5 = call %Result* @__quantum__rt__result_get_zero()
  %6 = call i1 @__quantum__rt__result_equal(%Result* %s1, %Result* %5)
  %7 = xor i1 %6, true
  br label %condContinue__2

condContinue__2:                                  ; preds = %condTrue__2, %condTrue__1
  %8 = phi i1 [ %7, %condTrue__2 ], [ %3, %condTrue__1 ]
  %9 = xor i1 %8, true
  br i1 %9, label %condTrue__3, label %condContinue__3

condTrue__3:                                      ; preds = %condContinue__2
  %10 = call %Result* @__quantum__rt__result_get_zero()
  %11 = call i1 @__quantum__rt__result_equal(%Result* %s2, %Result* %10)
  %12 = xor i1 %11, true
  br label %condContinue__3

condContinue__3:                                  ; preds = %condTrue__3, %condContinue__2
  %13 = phi i1 [ %12, %condTrue__3 ], [ %8, %condContinue__2 ]
  %14 = xor i1 %13, true
  br i1 %14, label %condTrue__4, label %condContinue__4

condTrue__4:                                      ; preds = %condContinue__3
  %15 = call %Result* @__quantum__rt__result_get_zero()
  %16 = call i1 @__quantum__rt__result_equal(%Result* %s3, %Result* %15)
  %17 = xor i1 %16, true
  br label %condContinue__4

condContinue__4:                                  ; preds = %condTrue__4, %condContinue__3
  %18 = phi i1 [ %17, %condTrue__4 ], [ %13, %condContinue__3 ]
  br label %condContinue__1

condContinue__1:                                  ; preds = %condContinue__4, %entry
  %19 = phi i1 [ %18, %condContinue__4 ], [ %0, %entry ]
  br i1 %19, label %then0__1, label %continue__1

then0__1:                                         ; preds = %condContinue__1
  call void @Microsoft__Quantum__Intrinsic__Reset__body(%Qubit* %q0)
  %20 = sub i64 %maxNIterations, 1
  call void @Microsoft__Quantum__Samples__Distill__body(i64 %20, %Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4)
  call void @__quantum__rt__result_update_reference_count(%Result* %s0, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s1, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s2, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s3, i32 -1)
  ret void

continue__1:                                      ; preds = %condContinue__1
  call void @__quantum__rt__result_update_reference_count(%Result* %s0, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s1, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s2, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %s3, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Samples__PrepareNoisyT__body(%Qubit* %target) {
entry:
  call void @Microsoft__Quantum__Intrinsic__Ry__body(double 0x3FEE91F42805715E, %Qubit* %target)
  call void @Microsoft__Quantum__Intrinsic__Rz__body(double 0xC015FDBBE9BBA775, %Qubit* %target)
  ret void
}

define internal void @Microsoft__Quantum__Samples__Encode__adj(%Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4) {
entry:
  call void @__quantum__qis__y__body(%Qubit* %q4)
  call void @__quantum__qis__z__body(%Qubit* %q3)
  call void @__quantum__qis__x__body(%Qubit* %q2)
  call void @__quantum__qis__x__body(%Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q4)
  call void @__quantum__qis__h__body(%Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__SWAP__adj(%Qubit* %q3, %Qubit* %q4)
  call void @__quantum__qis__h__body(%Qubit* %q4)
  call void @__quantum__qis__h__body(%Qubit* %q3)
  call void @__quantum__qis__h__body(%Qubit* %q1)
  call void @__quantum__qis__h__body(%Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q3, %Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q1, %Qubit* %q4)
  call void @__quantum__qis__h__body(%Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q1, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q2)
  call void @__quantum__qis__h__body(%Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q0, %Qubit* %q1)
  call void @__quantum__qis__h__body(%Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q4, %Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q4, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q3, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q2, %Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q4, %Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q3, %Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %q1, %Qubit* %q0)
  ret void
}

define internal %Result* @Microsoft__Quantum__Measurement__MResetZ__body(%Qubit* %target) {
entry:
  %result = call %Result* @Microsoft__Quantum__Intrinsic__M__body(%Qubit* %target)
  %0 = call %Result* @__quantum__rt__result_get_one()
  %1 = call i1 @__quantum__rt__result_equal(%Result* %result, %Result* %0)
  br i1 %1, label %then0__1, label %continue__1

then0__1:                                         ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* %target)
  br label %continue__1

continue__1:                                      ; preds = %then0__1, %entry
  ret %Result* %result
}

declare %Result* @__quantum__rt__result_get_zero()

declare i1 @__quantum__rt__result_equal(%Result*, %Result*)

define internal void @Microsoft__Quantum__Intrinsic__Reset__body(%Qubit* %qubit) {
entry:
  %0 = call %Result* @Microsoft__Quantum__Intrinsic__M__body(%Qubit* %qubit)
  %1 = call %Result* @__quantum__rt__result_get_one()
  %2 = call i1 @__quantum__rt__result_equal(%Result* %0, %Result* %1)
  call void @__quantum__rt__result_update_reference_count(%Result* %0, i32 -1)
  br i1 %2, label %then0__1, label %continue__1

then0__1:                                         ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* %qubit)
  br label %continue__1

continue__1:                                      ; preds = %then0__1, %entry
  ret void
}

declare void @__quantum__rt__result_update_reference_count(%Result*, i32)

define internal void @Microsoft__Quantum__Samples__Encode__body(%Qubit* %q0, %Qubit* %q1, %Qubit* %q2, %Qubit* %q3, %Qubit* %q4) {
entry:
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q1, %Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q3, %Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q4, %Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q2, %Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q3, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q4, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q4, %Qubit* %q3)
  call void @__quantum__qis__h__body(%Qubit* %q0)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q0, %Qubit* %q1)
  call void @__quantum__qis__h__body(%Qubit* %q1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q0, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q1, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q0, %Qubit* %q3)
  call void @__quantum__qis__h__body(%Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q1, %Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q3, %Qubit* %q4)
  call void @__quantum__qis__h__body(%Qubit* %q0)
  call void @__quantum__qis__h__body(%Qubit* %q1)
  call void @__quantum__qis__h__body(%Qubit* %q3)
  call void @__quantum__qis__h__body(%Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__SWAP__body(%Qubit* %q3, %Qubit* %q4)
  call void @__quantum__qis__h__body(%Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q0, %Qubit* %q4)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q0, %Qubit* %q3)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q0, %Qubit* %q2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %q0, %Qubit* %q1)
  call void @__quantum__qis__x__body(%Qubit* %q1)
  call void @__quantum__qis__x__body(%Qubit* %q2)
  call void @__quantum__qis__z__body(%Qubit* %q3)
  call void @__quantum__qis__y__body(%Qubit* %q4)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control, %Qubit* %target) {
entry:
  %__controlQubits__ = call %Array* @__quantum__rt__array_create_1d(i32 8, i64 1)
  %0 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %__controlQubits__, i64 0)
  %1 = bitcast i8* %0 to %Qubit**
  store %Qubit* %control, %Qubit** %1, align 8
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__x__ctl(%Array* %__controlQubits__, %Qubit* %target)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_reference_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

declare void @__quantum__qis__h__body(%Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__SWAP__body(%Qubit* %qubit1, %Qubit* %qubit2) {
entry:
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %qubit1, %Qubit* %qubit2)
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %qubit2, %Qubit* %qubit1)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %qubit1, %Qubit* %qubit2)
  ret void
}

declare void @__quantum__qis__x__body(%Qubit*)

declare void @__quantum__qis__z__body(%Qubit*)

declare void @__quantum__qis__y__body(%Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %control, %Qubit* %target) {
entry:
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control, %Qubit* %target)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__SWAP__adj(%Qubit* %qubit1, %Qubit* %qubit2) {
entry:
  call void @Microsoft__Quantum__Intrinsic__SWAP__body(%Qubit* %qubit1, %Qubit* %qubit2)
  ret void
}

define internal void @Microsoft__Quantum__Samples__Encode__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 0
  %q0 = load %Qubit*, %Qubit** %1, align 8
  %2 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 1
  %q1 = load %Qubit*, %Qubit** %2, align 8
  %3 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 2
  %q2 = load %Qubit*, %Qubit** %3, align 8
  %4 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 3
  %q3 = load %Qubit*, %Qubit** %4, align 8
  %5 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 4
  %q4 = load %Qubit*, %Qubit** %5, align 8
  %6 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %7 = bitcast %Tuple* %6 to { %Qubit*, %Qubit* }*
  %8 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %7, i32 0, i32 0
  %9 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %7, i32 0, i32 1
  store %Qubit* %q1, %Qubit** %8, align 8
  store %Qubit* %q0, %Qubit** %9, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %7)
  %10 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %11 = bitcast %Tuple* %10 to { %Qubit*, %Qubit* }*
  %12 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %11, i32 0, i32 0
  %13 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %11, i32 0, i32 1
  store %Qubit* %q3, %Qubit** %12, align 8
  store %Qubit* %q0, %Qubit** %13, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %11)
  %14 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %15 = bitcast %Tuple* %14 to { %Qubit*, %Qubit* }*
  %16 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %15, i32 0, i32 0
  %17 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %15, i32 0, i32 1
  store %Qubit* %q4, %Qubit** %16, align 8
  store %Qubit* %q0, %Qubit** %17, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %15)
  %18 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %19 = bitcast %Tuple* %18 to { %Qubit*, %Qubit* }*
  %20 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %19, i32 0, i32 0
  %21 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %19, i32 0, i32 1
  store %Qubit* %q2, %Qubit** %20, align 8
  store %Qubit* %q1, %Qubit** %21, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %19)
  %22 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %23 = bitcast %Tuple* %22 to { %Qubit*, %Qubit* }*
  %24 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %23, i32 0, i32 0
  %25 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %23, i32 0, i32 1
  store %Qubit* %q3, %Qubit** %24, align 8
  store %Qubit* %q2, %Qubit** %25, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %23)
  %26 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %27 = bitcast %Tuple* %26 to { %Qubit*, %Qubit* }*
  %28 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %27, i32 0, i32 0
  %29 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %27, i32 0, i32 1
  store %Qubit* %q4, %Qubit** %28, align 8
  store %Qubit* %q2, %Qubit** %29, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %27)
  %30 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %31 = bitcast %Tuple* %30 to { %Qubit*, %Qubit* }*
  %32 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %31, i32 0, i32 0
  %33 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %31, i32 0, i32 1
  store %Qubit* %q4, %Qubit** %32, align 8
  store %Qubit* %q3, %Qubit** %33, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %31)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q0)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %34 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %35 = bitcast %Tuple* %34 to { %Qubit*, %Qubit* }*
  %36 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %35, i32 0, i32 0
  %37 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %35, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %36, align 8
  store %Qubit* %q1, %Qubit** %37, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %35)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %38 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %39 = bitcast %Tuple* %38 to { %Qubit*, %Qubit* }*
  %40 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %39, i32 0, i32 0
  %41 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %39, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %40, align 8
  store %Qubit* %q2, %Qubit** %41, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %39)
  %42 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %43 = bitcast %Tuple* %42 to { %Qubit*, %Qubit* }*
  %44 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %43, i32 0, i32 0
  %45 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %43, i32 0, i32 1
  store %Qubit* %q1, %Qubit** %44, align 8
  store %Qubit* %q2, %Qubit** %45, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %43)
  %46 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %47 = bitcast %Tuple* %46 to { %Qubit*, %Qubit* }*
  %48 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %47, i32 0, i32 0
  %49 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %47, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %48, align 8
  store %Qubit* %q3, %Qubit** %49, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %47)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q3)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %50 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %51 = bitcast %Tuple* %50 to { %Qubit*, %Qubit* }*
  %52 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %51, i32 0, i32 0
  %53 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %51, i32 0, i32 1
  store %Qubit* %q1, %Qubit** %52, align 8
  store %Qubit* %q4, %Qubit** %53, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %51)
  %54 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %55 = bitcast %Tuple* %54 to { %Qubit*, %Qubit* }*
  %56 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %55, i32 0, i32 0
  %57 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %55, i32 0, i32 1
  store %Qubit* %q3, %Qubit** %56, align 8
  store %Qubit* %q4, %Qubit** %57, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %55)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q0)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q3)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %58 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %59 = bitcast %Tuple* %58 to { %Qubit*, %Qubit* }*
  %60 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %59, i32 0, i32 0
  %61 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %59, i32 0, i32 1
  store %Qubit* %q3, %Qubit** %60, align 8
  store %Qubit* %q4, %Qubit** %61, align 8
  call void @Microsoft__Quantum__Intrinsic__SWAP__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %59)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %62 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %63 = bitcast %Tuple* %62 to { %Qubit*, %Qubit* }*
  %64 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %63, i32 0, i32 0
  %65 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %63, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %64, align 8
  store %Qubit* %q4, %Qubit** %65, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %63)
  %66 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %67 = bitcast %Tuple* %66 to { %Qubit*, %Qubit* }*
  %68 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %67, i32 0, i32 0
  %69 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %67, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %68, align 8
  store %Qubit* %q3, %Qubit** %69, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %67)
  %70 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %71 = bitcast %Tuple* %70 to { %Qubit*, %Qubit* }*
  %72 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %71, i32 0, i32 0
  %73 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %71, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %72, align 8
  store %Qubit* %q2, %Qubit** %73, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %71)
  %74 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %75 = bitcast %Tuple* %74 to { %Qubit*, %Qubit* }*
  %76 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %75, i32 0, i32 0
  %77 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %75, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %76, align 8
  store %Qubit* %q1, %Qubit** %77, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %75)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__x__ctl(%Array* %__controlQubits__, %Qubit* %q1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__x__ctl(%Array* %__controlQubits__, %Qubit* %q2)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__z__ctl(%Array* %__controlQubits__, %Qubit* %q3)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__y__ctl(%Array* %__controlQubits__, %Qubit* %q4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %6, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %10, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %14, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %18, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %22, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %26, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %30, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %34, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %38, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %42, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %46, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %50, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %54, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %58, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %62, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %66, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %70, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %74, i32 -1)
  ret void
}

declare void @__quantum__rt__array_update_alias_count(%Array*, i32)

define internal void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %0, i32 0, i32 0
  %control = load %Qubit*, %Qubit** %1, align 8
  %2 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %0, i32 0, i32 1
  %target = load %Qubit*, %Qubit** %2, align 8
  %3 = call %Array* @__quantum__rt__array_create_1d(i32 8, i64 1)
  %4 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %3, i64 0)
  %5 = bitcast i8* %4 to %Qubit**
  store %Qubit* %control, %Qubit** %5, align 8
  %__controlQubits__1 = call %Array* @__quantum__rt__array_concatenate(%Array* %__controlQubits__, %Array* %3)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__1, i32 1)
  call void @__quantum__qis__x__ctl(%Array* %__controlQubits__1, %Qubit* %target)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__1, i32 -1)
  call void @__quantum__rt__array_update_reference_count(%Array* %3, i32 -1)
  call void @__quantum__rt__array_update_reference_count(%Array* %__controlQubits__1, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

declare %Tuple* @__quantum__rt__tuple_create(i64)

declare void @__quantum__qis__h__ctl(%Array*, %Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__SWAP__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %0, i32 0, i32 0
  %qubit1 = load %Qubit*, %Qubit** %1, align 8
  %2 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %0, i32 0, i32 1
  %qubit2 = load %Qubit*, %Qubit** %2, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %qubit1, %Qubit* %qubit2)
  %3 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %4 = bitcast %Tuple* %3 to { %Qubit*, %Qubit* }*
  %5 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %4, i32 0, i32 0
  %6 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %4, i32 0, i32 1
  store %Qubit* %qubit2, %Qubit** %5, align 8
  store %Qubit* %qubit1, %Qubit** %6, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %4)
  call void @Microsoft__Quantum__Intrinsic__CNOT__adj(%Qubit* %qubit1, %Qubit* %qubit2)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %3, i32 -1)
  ret void
}

declare void @__quantum__qis__x__ctl(%Array*, %Qubit*)

declare void @__quantum__qis__z__ctl(%Array*, %Qubit*)

declare void @__quantum__qis__y__ctl(%Array*, %Qubit*)

declare void @__quantum__rt__tuple_update_reference_count(%Tuple*, i32)

define internal void @Microsoft__Quantum__Samples__Encode__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 0
  %q0 = load %Qubit*, %Qubit** %1, align 8
  %2 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 1
  %q1 = load %Qubit*, %Qubit** %2, align 8
  %3 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 2
  %q2 = load %Qubit*, %Qubit** %3, align 8
  %4 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 3
  %q3 = load %Qubit*, %Qubit** %4, align 8
  %5 = getelementptr inbounds { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }, { %Qubit*, %Qubit*, %Qubit*, %Qubit*, %Qubit* }* %0, i32 0, i32 4
  %q4 = load %Qubit*, %Qubit** %5, align 8
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__y__ctl(%Array* %__controlQubits__, %Qubit* %q4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__z__ctl(%Array* %__controlQubits__, %Qubit* %q3)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__x__ctl(%Array* %__controlQubits__, %Qubit* %q2)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__x__ctl(%Array* %__controlQubits__, %Qubit* %q1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %6 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %7 = bitcast %Tuple* %6 to { %Qubit*, %Qubit* }*
  %8 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %7, i32 0, i32 0
  %9 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %7, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %8, align 8
  store %Qubit* %q1, %Qubit** %9, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %7)
  %10 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %11 = bitcast %Tuple* %10 to { %Qubit*, %Qubit* }*
  %12 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %11, i32 0, i32 0
  %13 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %11, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %12, align 8
  store %Qubit* %q2, %Qubit** %13, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %11)
  %14 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %15 = bitcast %Tuple* %14 to { %Qubit*, %Qubit* }*
  %16 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %15, i32 0, i32 0
  %17 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %15, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %16, align 8
  store %Qubit* %q3, %Qubit** %17, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %15)
  %18 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %19 = bitcast %Tuple* %18 to { %Qubit*, %Qubit* }*
  %20 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %19, i32 0, i32 0
  %21 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %19, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %20, align 8
  store %Qubit* %q4, %Qubit** %21, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %19)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %22 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %23 = bitcast %Tuple* %22 to { %Qubit*, %Qubit* }*
  %24 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %23, i32 0, i32 0
  %25 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %23, i32 0, i32 1
  store %Qubit* %q3, %Qubit** %24, align 8
  store %Qubit* %q4, %Qubit** %25, align 8
  call void @Microsoft__Quantum__Intrinsic__SWAP__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %23)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q3)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q0)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %26 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %27 = bitcast %Tuple* %26 to { %Qubit*, %Qubit* }*
  %28 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %27, i32 0, i32 0
  %29 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %27, i32 0, i32 1
  store %Qubit* %q3, %Qubit** %28, align 8
  store %Qubit* %q4, %Qubit** %29, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %27)
  %30 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %31 = bitcast %Tuple* %30 to { %Qubit*, %Qubit* }*
  %32 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %31, i32 0, i32 0
  %33 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %31, i32 0, i32 1
  store %Qubit* %q1, %Qubit** %32, align 8
  store %Qubit* %q4, %Qubit** %33, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %31)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q3)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %34 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %35 = bitcast %Tuple* %34 to { %Qubit*, %Qubit* }*
  %36 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %35, i32 0, i32 0
  %37 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %35, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %36, align 8
  store %Qubit* %q3, %Qubit** %37, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %35)
  %38 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %39 = bitcast %Tuple* %38 to { %Qubit*, %Qubit* }*
  %40 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %39, i32 0, i32 0
  %41 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %39, i32 0, i32 1
  store %Qubit* %q1, %Qubit** %40, align 8
  store %Qubit* %q2, %Qubit** %41, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %39)
  %42 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %43 = bitcast %Tuple* %42 to { %Qubit*, %Qubit* }*
  %44 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %43, i32 0, i32 0
  %45 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %43, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %44, align 8
  store %Qubit* %q2, %Qubit** %45, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %43)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %46 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %47 = bitcast %Tuple* %46 to { %Qubit*, %Qubit* }*
  %48 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %47, i32 0, i32 0
  %49 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %47, i32 0, i32 1
  store %Qubit* %q0, %Qubit** %48, align 8
  store %Qubit* %q1, %Qubit** %49, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %47)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %q0)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  %50 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %51 = bitcast %Tuple* %50 to { %Qubit*, %Qubit* }*
  %52 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %51, i32 0, i32 0
  %53 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %51, i32 0, i32 1
  store %Qubit* %q4, %Qubit** %52, align 8
  store %Qubit* %q3, %Qubit** %53, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %51)
  %54 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %55 = bitcast %Tuple* %54 to { %Qubit*, %Qubit* }*
  %56 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %55, i32 0, i32 0
  %57 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %55, i32 0, i32 1
  store %Qubit* %q4, %Qubit** %56, align 8
  store %Qubit* %q2, %Qubit** %57, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %55)
  %58 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %59 = bitcast %Tuple* %58 to { %Qubit*, %Qubit* }*
  %60 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %59, i32 0, i32 0
  %61 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %59, i32 0, i32 1
  store %Qubit* %q3, %Qubit** %60, align 8
  store %Qubit* %q2, %Qubit** %61, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %59)
  %62 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %63 = bitcast %Tuple* %62 to { %Qubit*, %Qubit* }*
  %64 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %63, i32 0, i32 0
  %65 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %63, i32 0, i32 1
  store %Qubit* %q2, %Qubit** %64, align 8
  store %Qubit* %q1, %Qubit** %65, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %63)
  %66 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %67 = bitcast %Tuple* %66 to { %Qubit*, %Qubit* }*
  %68 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %67, i32 0, i32 0
  %69 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %67, i32 0, i32 1
  store %Qubit* %q4, %Qubit** %68, align 8
  store %Qubit* %q0, %Qubit** %69, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %67)
  %70 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %71 = bitcast %Tuple* %70 to { %Qubit*, %Qubit* }*
  %72 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %71, i32 0, i32 0
  %73 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %71, i32 0, i32 1
  store %Qubit* %q3, %Qubit** %72, align 8
  store %Qubit* %q0, %Qubit** %73, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %71)
  %74 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %75 = bitcast %Tuple* %74 to { %Qubit*, %Qubit* }*
  %76 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %75, i32 0, i32 0
  %77 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %75, i32 0, i32 1
  store %Qubit* %q1, %Qubit** %76, align 8
  store %Qubit* %q0, %Qubit** %77, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %75)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %6, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %10, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %14, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %18, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %22, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %26, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %30, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %34, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %38, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %42, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %46, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %50, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %54, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %58, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %62, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %66, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %70, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %74, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__CNOT__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %0, i32 0, i32 0
  %control = load %Qubit*, %Qubit** %1, align 8
  %2 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %0, i32 0, i32 1
  %target = load %Qubit*, %Qubit** %2, align 8
  %3 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %4 = bitcast %Tuple* %3 to { %Qubit*, %Qubit* }*
  %5 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %4, i32 0, i32 0
  %6 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %4, i32 0, i32 1
  store %Qubit* %control, %Qubit** %5, align 8
  store %Qubit* %target, %Qubit** %6, align 8
  call void @Microsoft__Quantum__Intrinsic__CNOT__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %3, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__SWAP__ctladj(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %0, i32 0, i32 0
  %qubit1 = load %Qubit*, %Qubit** %1, align 8
  %2 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %0, i32 0, i32 1
  %qubit2 = load %Qubit*, %Qubit** %2, align 8
  %3 = call %Tuple* @__quantum__rt__tuple_create(i64 mul nuw (i64 ptrtoint (i1** getelementptr (i1*, i1** null, i32 1) to i64), i64 2))
  %4 = bitcast %Tuple* %3 to { %Qubit*, %Qubit* }*
  %5 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %4, i32 0, i32 0
  %6 = getelementptr inbounds { %Qubit*, %Qubit* }, { %Qubit*, %Qubit* }* %4, i32 0, i32 1
  store %Qubit* %qubit1, %Qubit** %5, align 8
  store %Qubit* %qubit2, %Qubit** %6, align 8
  call void @Microsoft__Quantum__Intrinsic__SWAP__ctl(%Array* %__controlQubits__, { %Qubit*, %Qubit* }* %4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %3, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth4InX__body() {
entry:
  %q = call %Qubit* @__quantum__rt__qubit_allocate()
  call void @Microsoft__Quantum__Samples__PrepareDistilledT__body(i64 4, %Qubit* %q)
  %0 = call %Result* @Microsoft__Quantum__Measurement__MResetX__body(%Qubit* %q)
  call void @__quantum__rt__result_update_reference_count(%Result* %0, i32 -1)
  call void @__quantum__rt__qubit_release(%Qubit* %q)
  ret void
}

declare %Qubit* @__quantum__rt__qubit_allocate()

declare %Array* @__quantum__rt__qubit_allocate_array(i64)

declare void @__quantum__rt__qubit_release(%Qubit*)

define internal void @Microsoft__Quantum__Samples__PrepareDistilledT__body(i64 %maxDepth, %Qubit* %target) {
entry:
  %aux1 = call %Qubit* @__quantum__rt__qubit_allocate()
  %aux2 = call %Qubit* @__quantum__rt__qubit_allocate()
  %aux3 = call %Qubit* @__quantum__rt__qubit_allocate()
  %aux4 = call %Qubit* @__quantum__rt__qubit_allocate()
  call void @Microsoft__Quantum__Samples__Distill__body(i64 %maxDepth, %Qubit* %target, %Qubit* %aux1, %Qubit* %aux2, %Qubit* %aux3, %Qubit* %aux4)
  call void @__quantum__qis__h__body(%Qubit* %target)
  call void @__quantum__qis__y__body(%Qubit* %target)
  call void @__quantum__rt__qubit_release(%Qubit* %aux1)
  call void @__quantum__rt__qubit_release(%Qubit* %aux2)
  call void @__quantum__rt__qubit_release(%Qubit* %aux3)
  call void @__quantum__rt__qubit_release(%Qubit* %aux4)
  ret void
}

define internal %Result* @Microsoft__Quantum__Measurement__MResetX__body(%Qubit* %target) {
entry:
  %bases = call %Array* @__quantum__rt__array_create_1d(i32 1, i64 1)
  %0 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %bases, i64 0)
  %1 = bitcast i8* %0 to i2*
  %2 = load i2, i2* @PauliX, align 1
  store i2 %2, i2* %1, align 1
  call void @__quantum__rt__array_update_alias_count(%Array* %bases, i32 1)
  %qubits = call %Array* @__quantum__rt__array_create_1d(i32 8, i64 1)
  %3 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %4 = bitcast i8* %3 to %Qubit**
  store %Qubit* %target, %Qubit** %4, align 8
  call void @__quantum__rt__array_update_alias_count(%Array* %qubits, i32 1)
  %result = call %Result* @__quantum__qis__measure__body(%Array* %bases, %Array* %qubits)
  call void @__quantum__rt__array_update_alias_count(%Array* %bases, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %qubits, i32 -1)
  call void @__quantum__rt__array_update_reference_count(%Array* %bases, i32 -1)
  call void @__quantum__rt__array_update_reference_count(%Array* %qubits, i32 -1)
  call void @__quantum__qis__h__body(%Qubit* %target)
  %5 = call %Result* @__quantum__rt__result_get_one()
  %6 = call i1 @__quantum__rt__result_equal(%Result* %result, %Result* %5)
  br i1 %6, label %then0__1, label %continue__1

then0__1:                                         ; preds = %entry
  call void @__quantum__qis__x__body(%Qubit* %target)
  br label %continue__1

continue__1:                                      ; preds = %then0__1, %entry
  ret %Result* %result
}

define internal void @Microsoft__Quantum__Intrinsic__Ry__body(double %theta, %Qubit* %qubit) {
entry:
  %pauli = load i2, i2* @PauliY, align 1
  call void @__quantum__qis__r__body(i2 %pauli, double %theta, %Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Rz__body(double %theta, %Qubit* %qubit) {
entry:
  %pauli = load i2, i2* @PauliZ, align 1
  call void @__quantum__qis__r__body(i2 %pauli, double %theta, %Qubit* %qubit)
  ret void
}

declare %Array* @__quantum__rt__array_create_1d(i32, i64)

declare i8* @__quantum__rt__array_get_element_ptr_1d(%Array*, i64)

declare %Result* @__quantum__qis__measure__body(%Array*, %Array*)

declare void @__quantum__rt__array_update_reference_count(%Array*, i32)

declare %Result* @__quantum__rt__result_get_one()

define internal %Result* @Microsoft__Quantum__Intrinsic__M__body(%Qubit* %qubit) {
entry:
  %bases = call %Array* @__quantum__rt__array_create_1d(i32 1, i64 1)
  %0 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %bases, i64 0)
  %1 = bitcast i8* %0 to i2*
  %2 = load i2, i2* @PauliZ, align 1
  store i2 %2, i2* %1, align 1
  call void @__quantum__rt__array_update_alias_count(%Array* %bases, i32 1)
  %qubits = call %Array* @__quantum__rt__array_create_1d(i32 8, i64 1)
  %3 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %4 = bitcast i8* %3 to %Qubit**
  store %Qubit* %qubit, %Qubit** %4, align 8
  call void @__quantum__rt__array_update_alias_count(%Array* %qubits, i32 1)
  %5 = call %Result* @__quantum__qis__measure__body(%Array* %bases, %Array* %qubits)
  call void @__quantum__rt__array_update_alias_count(%Array* %bases, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %qubits, i32 -1)
  call void @__quantum__rt__array_update_reference_count(%Array* %bases, i32 -1)
  call void @__quantum__rt__array_update_reference_count(%Array* %qubits, i32 -1)
  ret %Result* %5
}

declare %Array* @__quantum__rt__array_concatenate(%Array*, %Array*)

define internal void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__h__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__h__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__H__ctl(%Array* %__controlQubits__, %Qubit* %qubit) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %qubit)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__H__ctladj(%Array* %__controlQubits__, %Qubit* %qubit) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__h__ctl(%Array* %__controlQubits__, %Qubit* %qubit)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal %Result* @Microsoft__Quantum__Intrinsic__Measure__body(%Array* %bases, %Array* %qubits) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %bases, i32 1)
  call void @__quantum__rt__array_update_alias_count(%Array* %qubits, i32 1)
  %0 = call %Result* @__quantum__qis__measure__body(%Array* %bases, %Array* %qubits)
  call void @__quantum__rt__array_update_alias_count(%Array* %bases, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %qubits, i32 -1)
  ret %Result* %0
}

define internal void @Microsoft__Quantum__Intrinsic__R__body(i2 %pauli, double %theta, %Qubit* %qubit) {
entry:
  call void @__quantum__qis__r__body(i2 %pauli, double %theta, %Qubit* %qubit)
  ret void
}

declare void @__quantum__qis__r__body(i2, double, %Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__R__adj(i2 %pauli, double %theta, %Qubit* %qubit) {
entry:
  call void @__quantum__qis__r__adj(i2 %pauli, double %theta, %Qubit* %qubit)
  ret void
}

declare void @__quantum__qis__r__adj(i2, double, %Qubit*)

define internal void @Microsoft__Quantum__Intrinsic__R__ctl(%Array* %__controlQubits__, { i2, double, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %0, i32 0, i32 0
  %pauli = load i2, i2* %1, align 1
  %2 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %0, i32 0, i32 1
  %theta = load double, double* %2, align 8
  %3 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %0, i32 0, i32 2
  %qubit = load %Qubit*, %Qubit** %3, align 8
  %4 = call %Tuple* @__quantum__rt__tuple_create(i64 ptrtoint ({ i2, double, %Qubit* }* getelementptr ({ i2, double, %Qubit* }, { i2, double, %Qubit* }* null, i32 1) to i64))
  %5 = bitcast %Tuple* %4 to { i2, double, %Qubit* }*
  %6 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %5, i32 0, i32 0
  %7 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %5, i32 0, i32 1
  %8 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %5, i32 0, i32 2
  store i2 %pauli, i2* %6, align 1
  store double %theta, double* %7, align 8
  store %Qubit* %qubit, %Qubit** %8, align 8
  call void @__quantum__qis__r__ctl(%Array* %__controlQubits__, { i2, double, %Qubit* }* %5)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %4, i32 -1)
  ret void
}

declare void @__quantum__qis__r__ctl(%Array*, { i2, double, %Qubit* }*)

define internal void @Microsoft__Quantum__Intrinsic__R__ctladj(%Array* %__controlQubits__, { i2, double, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %0, i32 0, i32 0
  %pauli = load i2, i2* %1, align 1
  %2 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %0, i32 0, i32 1
  %theta = load double, double* %2, align 8
  %3 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %0, i32 0, i32 2
  %qubit = load %Qubit*, %Qubit** %3, align 8
  %4 = call %Tuple* @__quantum__rt__tuple_create(i64 ptrtoint ({ i2, double, %Qubit* }* getelementptr ({ i2, double, %Qubit* }, { i2, double, %Qubit* }* null, i32 1) to i64))
  %5 = bitcast %Tuple* %4 to { i2, double, %Qubit* }*
  %6 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %5, i32 0, i32 0
  %7 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %5, i32 0, i32 1
  %8 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %5, i32 0, i32 2
  store i2 %pauli, i2* %6, align 1
  store double %theta, double* %7, align 8
  store %Qubit* %qubit, %Qubit** %8, align 8
  call void @__quantum__qis__r__ctladj(%Array* %__controlQubits__, { i2, double, %Qubit* }* %5)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %4, i32 -1)
  ret void
}

declare void @__quantum__qis__r__ctladj(%Array*, { i2, double, %Qubit* }*)

define internal void @Microsoft__Quantum__Intrinsic__Ry__adj(double %theta, %Qubit* %qubit) {
entry:
  %pauli = load i2, i2* @PauliY, align 1
  %theta__1 = fneg double %theta
  call void @__quantum__qis__r__body(i2 %pauli, double %theta__1, %Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Ry__ctl(%Array* %__controlQubits__, { double, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %0, i32 0, i32 0
  %theta = load double, double* %1, align 8
  %2 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %0, i32 0, i32 1
  %qubit = load %Qubit*, %Qubit** %2, align 8
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %pauli = load i2, i2* @PauliY, align 1
  %3 = call %Tuple* @__quantum__rt__tuple_create(i64 ptrtoint ({ i2, double, %Qubit* }* getelementptr ({ i2, double, %Qubit* }, { i2, double, %Qubit* }* null, i32 1) to i64))
  %4 = bitcast %Tuple* %3 to { i2, double, %Qubit* }*
  %5 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 0
  %6 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 1
  %7 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 2
  store i2 %pauli, i2* %5, align 1
  store double %theta, double* %6, align 8
  store %Qubit* %qubit, %Qubit** %7, align 8
  call void @__quantum__qis__r__ctl(%Array* %__controlQubits__, { i2, double, %Qubit* }* %4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %3, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Ry__ctladj(%Array* %__controlQubits__, { double, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %0, i32 0, i32 0
  %theta = load double, double* %1, align 8
  %2 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %0, i32 0, i32 1
  %qubit = load %Qubit*, %Qubit** %2, align 8
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %pauli = load i2, i2* @PauliY, align 1
  %theta__1 = fneg double %theta
  %3 = call %Tuple* @__quantum__rt__tuple_create(i64 ptrtoint ({ i2, double, %Qubit* }* getelementptr ({ i2, double, %Qubit* }, { i2, double, %Qubit* }* null, i32 1) to i64))
  %4 = bitcast %Tuple* %3 to { i2, double, %Qubit* }*
  %5 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 0
  %6 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 1
  %7 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 2
  store i2 %pauli, i2* %5, align 1
  store double %theta__1, double* %6, align 8
  store %Qubit* %qubit, %Qubit** %7, align 8
  call void @__quantum__qis__r__ctl(%Array* %__controlQubits__, { i2, double, %Qubit* }* %4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %3, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Rz__adj(double %theta, %Qubit* %qubit) {
entry:
  %pauli = load i2, i2* @PauliZ, align 1
  %theta__1 = fneg double %theta
  call void @__quantum__qis__r__body(i2 %pauli, double %theta__1, %Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Rz__ctl(%Array* %__controlQubits__, { double, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %0, i32 0, i32 0
  %theta = load double, double* %1, align 8
  %2 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %0, i32 0, i32 1
  %qubit = load %Qubit*, %Qubit** %2, align 8
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %pauli = load i2, i2* @PauliZ, align 1
  %3 = call %Tuple* @__quantum__rt__tuple_create(i64 ptrtoint ({ i2, double, %Qubit* }* getelementptr ({ i2, double, %Qubit* }, { i2, double, %Qubit* }* null, i32 1) to i64))
  %4 = bitcast %Tuple* %3 to { i2, double, %Qubit* }*
  %5 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 0
  %6 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 1
  %7 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 2
  store i2 %pauli, i2* %5, align 1
  store double %theta, double* %6, align 8
  store %Qubit* %qubit, %Qubit** %7, align 8
  call void @__quantum__qis__r__ctl(%Array* %__controlQubits__, { i2, double, %Qubit* }* %4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %3, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Rz__ctladj(%Array* %__controlQubits__, { double, %Qubit* }* %0) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %1 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %0, i32 0, i32 0
  %theta = load double, double* %1, align 8
  %2 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %0, i32 0, i32 1
  %qubit = load %Qubit*, %Qubit** %2, align 8
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  %pauli = load i2, i2* @PauliZ, align 1
  %theta__1 = fneg double %theta
  %3 = call %Tuple* @__quantum__rt__tuple_create(i64 ptrtoint ({ i2, double, %Qubit* }* getelementptr ({ i2, double, %Qubit* }, { i2, double, %Qubit* }* null, i32 1) to i64))
  %4 = bitcast %Tuple* %3 to { i2, double, %Qubit* }*
  %5 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 0
  %6 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 1
  %7 = getelementptr inbounds { i2, double, %Qubit* }, { i2, double, %Qubit* }* %4, i32 0, i32 2
  store i2 %pauli, i2* %5, align 1
  store double %theta__1, double* %6, align 8
  store %Qubit* %qubit, %Qubit** %7, align 8
  call void @__quantum__qis__r__ctl(%Array* %__controlQubits__, { i2, double, %Qubit* }* %4)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  call void @__quantum__rt__tuple_update_reference_count(%Tuple* %3, i32 -1)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__X__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__x__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__X__adj(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__x__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__X__ctl(%Array* %__controlQubits__, %Qubit* %qubit) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__x__ctl(%Array* %__controlQubits__, %Qubit* %qubit)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__X__ctladj(%Array* %__controlQubits__, %Qubit* %qubit) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__x__ctl(%Array* %__controlQubits__, %Qubit* %qubit)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Y__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__y__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Y__adj(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__y__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Y__ctl(%Array* %__controlQubits__, %Qubit* %qubit) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__y__ctl(%Array* %__controlQubits__, %Qubit* %qubit)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Y__ctladj(%Array* %__controlQubits__, %Qubit* %qubit) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__y__ctl(%Array* %__controlQubits__, %Qubit* %qubit)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Z__body(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__z__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Z__adj(%Qubit* %qubit) {
entry:
  call void @__quantum__qis__z__body(%Qubit* %qubit)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Z__ctl(%Array* %__controlQubits__, %Qubit* %qubit) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__z__ctl(%Array* %__controlQubits__, %Qubit* %qubit)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define internal void @Microsoft__Quantum__Intrinsic__Z__ctladj(%Array* %__controlQubits__, %Qubit* %qubit) {
entry:
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 1)
  call void @__quantum__qis__z__ctl(%Array* %__controlQubits__, %Qubit* %qubit)
  call void @__quantum__rt__array_update_alias_count(%Array* %__controlQubits__, i32 -1)
  ret void
}

define void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth4InX__Interop() #0 {
entry:
  call void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth4InX__body()
  ret void
}

define void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth4InX() #1 {
entry:
  call void @Microsoft__Quantum__Samples__MeasureDistilledTAtDepth4InX__body()
  %0 = call %String* @__quantum__rt__string_create(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @0, i32 0, i32 0))
  call void @__quantum__rt__message(%String* %0)
  call void @__quantum__rt__string_update_reference_count(%String* %0, i32 -1)
  ret void
}

declare void @__quantum__rt__message(%String*)

declare %String* @__quantum__rt__string_create(i8*)

declare void @__quantum__rt__string_update_reference_count(%String*, i32)

attributes #0 = { "InteropFriendly" }
attributes #1 = { "EntryPoint" }

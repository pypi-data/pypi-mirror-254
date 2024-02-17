; ModuleID = 'RandomWalkPE1.ll'
source_filename = "RandomWalkPE1.ll"

%Tuple = type opaque
%Qubit = type opaque
%Array = type opaque
%Result = type opaque
%Callable = type opaque
%String = type opaque

@Microsoft__Quantum__Intrinsic__Rz = internal constant [4 x void (%Tuple*, %Tuple*, %Tuple*)*] undef

declare %Qubit* @__quantum__rt__qubit_allocate() local_unnamed_addr

declare %Array* @__quantum__rt__qubit_allocate_array(i64) local_unnamed_addr

declare void @__quantum__rt__qubit_release(%Qubit*) local_unnamed_addr

declare %Result* @__quantum__rt__result_get_zero() local_unnamed_addr

declare i1 @__quantum__rt__result_equal(%Result*, %Result*) local_unnamed_addr

declare void @__quantum__rt__result_update_reference_count(%Result*, i32) local_unnamed_addr

declare %Array* @__quantum__rt__array_create_1d(i32, i64) local_unnamed_addr

declare i8* @__quantum__rt__array_get_element_ptr_1d(%Array*, i64) local_unnamed_addr

declare %Tuple* @__quantum__rt__tuple_create(i64) local_unnamed_addr

declare %Result* @__quantum__qis__m__body(%Qubit*) local_unnamed_addr

declare void @__quantum__rt__array_update_reference_count(%Array*, i32) local_unnamed_addr

declare void @__quantum__rt__tuple_update_reference_count(%Tuple*, i32) local_unnamed_addr

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__rt__array_update_alias_count(%Array*, i32) local_unnamed_addr

declare i64 @__quantum__rt__array_get_size_1d(%Array*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare %Array* @__quantum__rt__array_concatenate(%Array*, %Array*) local_unnamed_addr

declare %Callable* @__quantum__rt__callable_create([4 x void (%Tuple*, %Tuple*, %Tuple*)*]*, [2 x void (%Tuple*, i32)*]*, %Tuple*) local_unnamed_addr

declare void @__quantum__rt__callable_make_controlled(%Callable*) local_unnamed_addr

declare void @__quantum__rt__capture_update_reference_count(%Callable*, i32) local_unnamed_addr

declare void @__quantum__rt__callable_update_reference_count(%Callable*, i32) local_unnamed_addr

declare void @__quantum__qis__rz__body(double, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__t__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__t__adj(%Qubit*) local_unnamed_addr

declare void @__quantum__rt__capture_update_alias_count(%Callable*, i32) local_unnamed_addr

declare void @__quantum__rt__callable_update_alias_count(%Callable*, i32) local_unnamed_addr

declare void @__quantum__rt__tuple_update_alias_count(%Tuple*, i32) local_unnamed_addr

declare void @__quantum__rt__qubit_release_array(%Array*) local_unnamed_addr

declare void @__quantum__rt__callable_invoke(%Callable*, %Tuple*, %Tuple*) local_unnamed_addr

define void @Microsoft__Quantum__Qir__Emission__EstimatePhaseByRandomWalk(i64 %nrIter) local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__h__body(%Qubit* null)
  %.not1.i = icmp slt i64 %nrIter, 1
  br i1 %.not1.i, label %Microsoft__Quantum__Qir__Emission__EstimatePhaseByRandomWalk__body.1.exit, label %body__1.i

body__1.i:                                        ; preds = %entry, %body__1.body__1_crit_edge.i
  %.phi.i = phi i64 [ %.0.i, %body__1.body__1_crit_edge.i ], [ 2, %entry ]
  %sigma.03.i = phi double [ %78, %body__1.body__1_crit_edge.i ], [ 6.065000e-01, %entry ]
  %mu.02.i = phi double [ %77, %body__1.body__1_crit_edge.i ], [ 7.951000e-01, %entry ]
  %0 = fmul double %sigma.03.i, 0x400921FB54442D18
  %1 = fmul double %0, 5.000000e-01
  %time.i = fsub double %mu.02.i, %1
  tail call void @__quantum__qis__h__body(%Qubit* null)
  %2 = fdiv double -1.000000e+00, %sigma.03.i
  %3 = fmul double %2, %time.i
  tail call void @__quantum__qis__rz__body(double %3, %Qubit* null)
  %4 = tail call %Array* @__quantum__rt__array_create_1d(i32 8, i64 1)
  %5 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %4, i64 0)
  %6 = bitcast i8* %5 to %Qubit**
  store %Qubit* null, %Qubit** %6, align 8
  %7 = tail call %Tuple* @__quantum__rt__tuple_create(i64 16)
  %8 = bitcast %Tuple* %7 to { double, %Qubit* }*
  %9 = bitcast %Tuple* %7 to double*
  %10 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %8, i64 0, i32 1
  %11 = fmul double %time.i, 0x400921FB54442D18
  store double %11, double* %9, align 8
  store %Qubit* null, %Qubit** %10, align 8
  %theta.i.i = load double, double* %9, align 8
  %12 = tail call i64 @__quantum__rt__array_get_size_1d(%Array* %4)
  %13 = icmp eq i64 %12, 0
  br i1 %13, label %then0__1.i.i, label %test1__1.i.i

then0__1.i.i:                                     ; preds = %body__1.i
  tail call void @__quantum__qis__rz__body(double %theta.i.i, %Qubit* null)
  br label %Microsoft__Quantum__Intrinsic__Rz__ctl.2.exit.i

test1__1.i.i:                                     ; preds = %body__1.i
  %14 = tail call i64 @__quantum__rt__array_get_size_1d(%Array* %4)
  %15 = icmp eq i64 %14, 1
  br i1 %15, label %then1__1.i.i, label %else__1.i.i

then1__1.i.i:                                     ; preds = %test1__1.i.i
  %16 = fmul double %theta.i.i, 5.000000e-01
  tail call void @__quantum__qis__rz__body(double %16, %Qubit* null)
  %17 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %4, i64 0)
  %18 = bitcast i8* %17 to %Qubit**
  %19 = load %Qubit*, %Qubit** %18, align 8
  tail call void @__quantum__qis__cnot__body(%Qubit* %19, %Qubit* null)
  %20 = fmul double %theta.i.i, -5.000000e-01
  tail call void @__quantum__qis__rz__body(double %20, %Qubit* null)
  %21 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %4, i64 0)
  %22 = bitcast i8* %21 to %Qubit**
  %23 = load %Qubit*, %Qubit** %22, align 8
  tail call void @__quantum__qis__cnot__body(%Qubit* %23, %Qubit* null)
  br label %Microsoft__Quantum__Intrinsic__Rz__ctl.2.exit.i

else__1.i.i:                                      ; preds = %test1__1.i.i
  %24 = tail call %Callable* @__quantum__rt__callable_create([4 x void (%Tuple*, %Tuple*, %Tuple*)*]* nonnull @Microsoft__Quantum__Intrinsic__Rz, [2 x void (%Tuple*, i32)*]* null, %Tuple* null)
  tail call void @__quantum__rt__callable_make_controlled(%Callable* %24)
  %25 = tail call %Tuple* @__quantum__rt__tuple_create(i64 16)
  %26 = bitcast %Tuple* %25 to { %Array*, { double, %Qubit* }* }*
  %27 = bitcast %Tuple* %25 to %Array**
  %28 = getelementptr inbounds { %Array*, { double, %Qubit* }* }, { %Array*, { double, %Qubit* }* }* %26, i64 0, i32 1
  %29 = tail call %Tuple* @__quantum__rt__tuple_create(i64 16)
  %30 = bitcast %Tuple* %29 to { double, %Qubit* }*
  %31 = bitcast %Tuple* %29 to double*
  %32 = getelementptr inbounds { double, %Qubit* }, { double, %Qubit* }* %30, i64 0, i32 1
  store double %theta.i.i, double* %31, align 8
  store %Qubit* null, %Qubit** %32, align 8
  store %Array* %4, %Array** %27, align 8
  %33 = bitcast { double, %Qubit* }** %28 to %Tuple**
  store %Tuple* %29, %Tuple** %33, align 8
  tail call void @__quantum__rt__capture_update_alias_count(%Callable* %24, i32 1)
  tail call void @__quantum__rt__callable_update_alias_count(%Callable* %24, i32 1)
  %controls.i.i.i = load %Array*, %Array** %27, align 8
  %arg.i.i.i = load { double, %Qubit* }*, { double, %Qubit* }** %28, align 8
  %34 = bitcast { double, %Qubit* }* %arg.i.i.i to %Tuple*
  tail call void @__quantum__rt__tuple_update_alias_count(%Tuple* %34, i32 1)
  %numControls.i.i.i = tail call i64 @__quantum__rt__array_get_size_1d(%Array* %controls.i.i.i)
  %numControlPairs.i.i.i = sdiv i64 %numControls.i.i.i, 2
  %temps.i.i.i = tail call %Array* @__quantum__rt__qubit_allocate_array(i64 %numControlPairs.i.i.i)
  %.not.not1.i.i.i = icmp sgt i64 %numControls.i.i.i, 1
  br i1 %.not.not1.i.i.i, label %body__1.i.i.i, label %exit__1.i.i.i

body__1.i.i.i:                                    ; preds = %else__1.i.i, %body__1.i.i.i
  %__qsVar0__numPair__2.i.i.i = phi i64 [ %46, %body__1.i.i.i ], [ 0, %else__1.i.i ]
  %35 = shl nuw i64 %__qsVar0__numPair__2.i.i.i, 1
  %36 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %controls.i.i.i, i64 %35)
  %37 = bitcast i8* %36 to %Qubit**
  %38 = load %Qubit*, %Qubit** %37, align 8
  %39 = or i64 %35, 1
  %40 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %controls.i.i.i, i64 %39)
  %41 = bitcast i8* %40 to %Qubit**
  %42 = load %Qubit*, %Qubit** %41, align 8
  %43 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %temps.i.i.i, i64 %__qsVar0__numPair__2.i.i.i)
  %44 = bitcast i8* %43 to %Qubit**
  %45 = load %Qubit*, %Qubit** %44, align 8
  tail call void @__quantum__qis__h__body(%Qubit* %45)
  tail call void @__quantum__qis__cnot__body(%Qubit* %45, %Qubit* %38)
  tail call void @__quantum__qis__cnot__body(%Qubit* %38, %Qubit* %42)
  tail call void @__quantum__qis__t__body(%Qubit* %42)
  tail call void @__quantum__qis__t__adj(%Qubit* %38)
  tail call void @__quantum__qis__t__body(%Qubit* %45)
  tail call void @__quantum__qis__cnot__body(%Qubit* %45, %Qubit* %38)
  tail call void @__quantum__qis__cnot__body(%Qubit* %38, %Qubit* %42)
  tail call void @__quantum__qis__t__adj(%Qubit* %42)
  tail call void @__quantum__qis__cnot__body(%Qubit* %45, %Qubit* %42)
  tail call void @__quantum__qis__h__body(%Qubit* %45)
  %46 = add nuw nsw i64 %__qsVar0__numPair__2.i.i.i, 1
  %.not.not.i.i.i = icmp slt i64 %46, %numControlPairs.i.i.i
  br i1 %.not.not.i.i.i, label %body__1.i.i.i, label %exit__1.i.i.i

exit__1.i.i.i:                                    ; preds = %body__1.i.i.i, %else__1.i.i
  %47 = and i64 %numControls.i.i.i, 1
  %48 = icmp eq i64 %47, 0
  br i1 %48, label %condContinue__1.i.i.i, label %condFalse__1.i.i.i

condFalse__1.i.i.i:                               ; preds = %exit__1.i.i.i
  %49 = tail call %Array* @__quantum__rt__array_create_1d(i32 8, i64 1)
  %50 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %49, i64 0)
  %51 = bitcast i8* %50 to %Qubit**
  %52 = add i64 %numControls.i.i.i, -1
  %53 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %controls.i.i.i, i64 %52)
  %54 = bitcast i8* %53 to %Qubit**
  %55 = load %Qubit*, %Qubit** %54, align 8
  store %Qubit* %55, %Qubit** %51, align 8
  %56 = tail call %Array* @__quantum__rt__array_concatenate(%Array* %temps.i.i.i, %Array* %49)
  br label %condContinue__1.i.i.i

condContinue__1.i.i.i:                            ; preds = %condFalse__1.i.i.i, %exit__1.i.i.i
  %__qsVar1__newControls__.i.i.i = phi %Array* [ %56, %condFalse__1.i.i.i ], [ %temps.i.i.i, %exit__1.i.i.i ]
  %57 = tail call %Tuple* @__quantum__rt__tuple_create(i64 16)
  %58 = bitcast %Tuple* %57 to { %Array*, { double, %Qubit* }* }*
  %59 = bitcast %Tuple* %57 to %Array**
  %60 = getelementptr inbounds { %Array*, { double, %Qubit* }* }, { %Array*, { double, %Qubit* }* }* %58, i64 0, i32 1
  tail call void @__quantum__rt__tuple_update_reference_count(%Tuple* %34, i32 1)
  store %Array* %__qsVar1__newControls__.i.i.i, %Array** %59, align 8
  store { double, %Qubit* }* %arg.i.i.i, { double, %Qubit* }** %60, align 8
  tail call void @__quantum__rt__callable_invoke(%Callable* %24, %Tuple* %57, %Tuple* null)
  br i1 %.not.not1.i.i.i, label %body__2.preheader.i.i.i, label %Microsoft__Quantum__Intrinsic___5c2cfe0afdbb482b89fbe4e914873170___QsRef23__ApplyWithLessControlsA____body.3.exit.i.i

body__2.preheader.i.i.i:                          ; preds = %condContinue__1.i.i.i
  %__qsVar0____qsVar0__numPair____3.i.i.i = add nsw i64 %numControlPairs.i.i.i, -1
  br label %body__2.i.i.i

body__2.i.i.i:                                    ; preds = %body__2.i.i.i, %body__2.preheader.i.i.i
  %__qsVar0____qsVar0__numPair____4.i.i.i = phi i64 [ %__qsVar0____qsVar0__numPair____.i.i.i, %body__2.i.i.i ], [ %__qsVar0____qsVar0__numPair____3.i.i.i, %body__2.preheader.i.i.i ]
  %61 = shl nuw i64 %__qsVar0____qsVar0__numPair____4.i.i.i, 1
  %62 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %controls.i.i.i, i64 %61)
  %63 = bitcast i8* %62 to %Qubit**
  %64 = load %Qubit*, %Qubit** %63, align 8
  %65 = or i64 %61, 1
  %66 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %controls.i.i.i, i64 %65)
  %67 = bitcast i8* %66 to %Qubit**
  %68 = load %Qubit*, %Qubit** %67, align 8
  %69 = tail call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %temps.i.i.i, i64 %__qsVar0____qsVar0__numPair____4.i.i.i)
  %70 = bitcast i8* %69 to %Qubit**
  %71 = load %Qubit*, %Qubit** %70, align 8
  tail call void @__quantum__qis__h__body(%Qubit* %71)
  tail call void @__quantum__qis__cnot__body(%Qubit* %71, %Qubit* %68)
  tail call void @__quantum__qis__t__body(%Qubit* %68)
  tail call void @__quantum__qis__cnot__body(%Qubit* %64, %Qubit* %68)
  tail call void @__quantum__qis__cnot__body(%Qubit* %71, %Qubit* %64)
  tail call void @__quantum__qis__t__adj(%Qubit* %71)
  tail call void @__quantum__qis__t__body(%Qubit* %64)
  tail call void @__quantum__qis__t__adj(%Qubit* %68)
  tail call void @__quantum__qis__cnot__body(%Qubit* %64, %Qubit* %68)
  tail call void @__quantum__qis__cnot__body(%Qubit* %71, %Qubit* %64)
  tail call void @__quantum__qis__h__body(%Qubit* %71)
  %__qsVar0____qsVar0__numPair____.i.i.i = add i64 %__qsVar0____qsVar0__numPair____4.i.i.i, -1
  %72 = icmp sgt i64 %__qsVar0____qsVar0__numPair____.i.i.i, -1
  br i1 %72, label %body__2.i.i.i, label %Microsoft__Quantum__Intrinsic___5c2cfe0afdbb482b89fbe4e914873170___QsRef23__ApplyWithLessControlsA____body.3.exit.i.i

Microsoft__Quantum__Intrinsic___5c2cfe0afdbb482b89fbe4e914873170___QsRef23__ApplyWithLessControlsA____body.3.exit.i.i: ; preds = %body__2.i.i.i, %condContinue__1.i.i.i
  tail call void @__quantum__rt__tuple_update_reference_count(%Tuple* %34, i32 -1)
  tail call void @__quantum__rt__tuple_update_reference_count(%Tuple* %57, i32 -1)
  tail call void @__quantum__rt__qubit_release_array(%Array* %temps.i.i.i)
  tail call void @__quantum__rt__capture_update_alias_count(%Callable* %24, i32 -1)
  tail call void @__quantum__rt__callable_update_alias_count(%Callable* %24, i32 -1)
  tail call void @__quantum__rt__tuple_update_alias_count(%Tuple* %34, i32 -1)
  tail call void @__quantum__rt__capture_update_reference_count(%Callable* %24, i32 -1)
  tail call void @__quantum__rt__callable_update_reference_count(%Callable* %24, i32 -1)
  tail call void @__quantum__rt__tuple_update_reference_count(%Tuple* %29, i32 -1)
  tail call void @__quantum__rt__tuple_update_reference_count(%Tuple* %25, i32 -1)
  br label %Microsoft__Quantum__Intrinsic__Rz__ctl.2.exit.i

Microsoft__Quantum__Intrinsic__Rz__ctl.2.exit.i:  ; preds = %Microsoft__Quantum__Intrinsic___5c2cfe0afdbb482b89fbe4e914873170___QsRef23__ApplyWithLessControlsA____body.3.exit.i.i, %then1__1.i.i, %then0__1.i.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  tail call void @__quantum__rt__tuple_update_reference_count(%Tuple* %7, i32 -1)
  %73 = tail call %Result* @__quantum__rt__result_get_zero()
  %74 = tail call i1 @__quantum__rt__result_equal(%Result* null, %Result* %73)
  %75 = fmul double %sigma.03.i, 6.065000e-01
  %76 = fneg double %75
  %.p.i = select i1 %74, double %76, double %75
  %77 = fadd double %mu.02.i, %.p.i
  %.not.i = icmp sgt i64 %.phi.i, %nrIter
  br i1 %.not.i, label %Microsoft__Quantum__Qir__Emission__EstimatePhaseByRandomWalk__body.1.exit, label %body__1.body__1_crit_edge.i

body__1.body__1_crit_edge.i:                      ; preds = %Microsoft__Quantum__Intrinsic__Rz__ctl.2.exit.i
  %78 = fmul double %sigma.03.i, 7.951000e-01
  %.0.i = add i64 %.phi.i, 1
  br label %body__1.i

Microsoft__Quantum__Qir__Emission__EstimatePhaseByRandomWalk__body.1.exit: ; preds = %Microsoft__Quantum__Intrinsic__Rz__ctl.2.exit.i, %entry
  %mu.0.lcssa.i = phi double [ 7.951000e-01, %entry ], [ %77, %Microsoft__Quantum__Intrinsic__Rz__ctl.2.exit.i ]
  %79 = tail call %String* @__quantum__rt__double_to_string(double %mu.0.lcssa.i)
  ret void
}

declare void @__quantum__rt__message(%String*) local_unnamed_addr

declare %String* @__quantum__rt__double_to_string(double) local_unnamed_addr

declare void @__quantum__rt__string_update_reference_count(%String*, i32) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="1" }


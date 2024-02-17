; ModuleID = 'mutables_ops_branches.ll'
source_filename = "mutables_ops_branches.ll"

%Qubit = type opaque
%Result = type opaque
%String = type opaque

@0 = internal constant [3 x i8] c"()\00"

declare %Qubit* @__quantum__rt__qubit_allocate() local_unnamed_addr

declare void @__quantum__rt__qubit_release(%Qubit*) local_unnamed_addr

declare %Result* @__quantum__qis__m__body(%Qubit*) local_unnamed_addr

declare void @__quantum__rt__result_update_reference_count(%Result*, i32) local_unnamed_addr

declare %Result* @__quantum__rt__result_get_zero() local_unnamed_addr

declare i1 @__quantum__rt__result_equal(%Result*, %Result*) local_unnamed_addr

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare %String* @__quantum__rt__string_create(i8*) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

define void @mutables_ops_branches__HelloQ() local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %0 = tail call %Result* @__quantum__rt__result_get_zero()
  %1 = tail call i1 @__quantum__rt__result_equal(%Result* null, %Result* %0)
  br i1 %1, label %then0__1.i.i, label %exiting__1.i.i

then0__1.i.i:                                     ; preds = %entry
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.i

exiting__1.i.i:                                   ; preds = %then0__1.i.i, %entry
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 1 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %2 = tail call %Result* @__quantum__rt__result_get_zero()
  %3 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 1 to %Result*), %Result* %2)
  br i1 %3, label %then0__1.i.14.i, label %exiting__1.i.15.i

body__1.i.preheader.1.i:                          ; preds = %then0__1.i.28.i, %exiting__1.i.15.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 3 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %4 = tail call %Result* @__quantum__rt__result_get_zero()
  %5 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 3 to %Result*), %Result* %4)
  br i1 %5, label %then0__1.i.1.i, label %exiting__1.i.1.i

then0__1.i.1.i:                                   ; preds = %body__1.i.preheader.1.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.1.i

exiting__1.i.1.i:                                 ; preds = %then0__1.i.1.i, %body__1.i.preheader.1.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 4 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %6 = tail call %Result* @__quantum__rt__result_get_zero()
  %7 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 4 to %Result*), %Result* %6)
  br i1 %7, label %then0__1.i.1.1.i, label %exiting__1.i.1.1.i

body__1.i.preheader.2.i:                          ; preds = %then0__1.i.1.3.i, %exiting__1.i.1.2.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 7 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %8 = tail call %Result* @__quantum__rt__result_get_zero()
  %9 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 7 to %Result*), %Result* %8)
  br i1 %9, label %then0__1.i.2.i, label %exiting__1.i.2.i

then0__1.i.2.i:                                   ; preds = %body__1.i.preheader.2.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.2.i

exiting__1.i.2.i:                                 ; preds = %then0__1.i.2.i, %body__1.i.preheader.2.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 8 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %10 = tail call %Result* @__quantum__rt__result_get_zero()
  %11 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 8 to %Result*), %Result* %10)
  br i1 %11, label %then0__1.i.2.1.i, label %exiting__1.i.2.1.i

then0__1.i.2.1.i:                                 ; preds = %exiting__1.i.2.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.2.1.i

exiting__1.i.2.1.i:                               ; preds = %then0__1.i.2.1.i, %exiting__1.i.2.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 9 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %12 = tail call %Result* @__quantum__rt__result_get_zero()
  %13 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 9 to %Result*), %Result* %12)
  br i1 %13, label %then0__1.i.2.2.i, label %exiting__1.i.2.2.i

then0__1.i.2.2.i:                                 ; preds = %exiting__1.i.2.1.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.2.2.i

exiting__1.i.2.2.i:                               ; preds = %then0__1.i.2.2.i, %exiting__1.i.2.1.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 10 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %14 = tail call %Result* @__quantum__rt__result_get_zero()
  %15 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 10 to %Result*), %Result* %14)
  br i1 %15, label %then0__1.i.2.3.i, label %exiting__1.i.2.3.i

then0__1.i.2.3.i:                                 ; preds = %exiting__1.i.2.2.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.2.3.i

exiting__1.i.2.3.i:                               ; preds = %then0__1.i.2.3.i, %exiting__1.i.2.2.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 11 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %16 = tail call %Result* @__quantum__rt__result_get_zero()
  %17 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 11 to %Result*), %Result* %16)
  br i1 %17, label %then0__1.i.2.4.i, label %mutables_ops_branches__HelloQ__body.1.exit

then0__1.i.2.4.i:                                 ; preds = %exiting__1.i.2.3.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %mutables_ops_branches__HelloQ__body.1.exit

then0__1.i.1.1.i:                                 ; preds = %exiting__1.i.1.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.1.1.i

exiting__1.i.1.1.i:                               ; preds = %then0__1.i.1.1.i, %exiting__1.i.1.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 5 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %18 = tail call %Result* @__quantum__rt__result_get_zero()
  %19 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 5 to %Result*), %Result* %18)
  br i1 %19, label %then0__1.i.1.2.i, label %exiting__1.i.1.2.i

then0__1.i.1.2.i:                                 ; preds = %exiting__1.i.1.1.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.1.2.i

exiting__1.i.1.2.i:                               ; preds = %then0__1.i.1.2.i, %exiting__1.i.1.1.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 6 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %20 = tail call %Result* @__quantum__rt__result_get_zero()
  %21 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 6 to %Result*), %Result* %20)
  br i1 %21, label %then0__1.i.1.3.i, label %body__1.i.preheader.2.i

then0__1.i.1.3.i:                                 ; preds = %exiting__1.i.1.2.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %body__1.i.preheader.2.i

then0__1.i.14.i:                                  ; preds = %exiting__1.i.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %exiting__1.i.15.i

exiting__1.i.15.i:                                ; preds = %then0__1.i.14.i, %exiting__1.i.i
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__cnot__body(%Qubit* null, %Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 2 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %22 = tail call %Result* @__quantum__rt__result_get_zero()
  %23 = tail call i1 @__quantum__rt__result_equal(%Result* nonnull inttoptr (i64 2 to %Result*), %Result* %22)
  br i1 %23, label %then0__1.i.28.i, label %body__1.i.preheader.1.i

then0__1.i.28.i:                                  ; preds = %exiting__1.i.15.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  br label %body__1.i.preheader.1.i

mutables_ops_branches__HelloQ__body.1.exit:       ; preds = %exiting__1.i.2.3.i, %then0__1.i.2.4.i
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* nonnull inttoptr (i64 12 to %Result*))
  ret void
}

declare void @__quantum__rt__message(%String*) local_unnamed_addr

declare void @__quantum__rt__string_update_reference_count(%String*, i32) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="2" }

